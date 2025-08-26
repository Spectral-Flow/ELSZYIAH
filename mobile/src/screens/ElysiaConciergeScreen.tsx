/**
 * The Avant Resident App - Elysia Concierge Interface
 * Kairoi Residential - Centennial, Colorado
 * 
 * Purpose: Native mobile interface for luxury apartment living
 * // @progress Resident mobile app initialization - 25%
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  TextInput,
  Alert,
  Platform
} from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Type definitions for The Avant
interface ResidentProfile {
  unitNumber: string;
  residentId: string;
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  emergencyContact: string;
  moveInDate: string;
  leaseEndDate: string;
}

interface ConciergeRequest {
  type: 'maintenance' | 'amenity_booking' | 'package_inquiry' | 'guest_access' | 'community_info' | 'general_inquiry';
  message: string;
  priority: 'low' | 'medium' | 'high' | 'urgent';
  preferredContact: 'app' | 'email' | 'phone';
}

interface ElysiaResponse {
  response: string;
  requestId: string;
  estimatedResolutionTime: string;
  followUpNeeded: boolean;
  escalationRequired: boolean;
}

// The Avant brand colors
const AvantColors = {
  primary: '#2C3E50',      // Sophisticated navy
  secondary: '#E8F4F8',    // Soft blue-gray
  accent: '#3498DB',       // Professional blue
  success: '#27AE60',      // Green for confirmations
  warning: '#F39C12',      // Orange for alerts
  error: '#E74C3C',        // Red for emergencies
  text: '#2C3E50',
  lightText: '#7F8C8D',
  background: '#FFFFFF',
  lightBackground: '#F8F9FA'
};

class AvantResidentAPI {
  private baseUrl = Platform.OS === 'android' ? 
    'http://10.0.2.2:8000' :  // Android emulator
    'http://localhost:8000';   // iOS simulator
  
  async submitRequest(request: ConciergeRequest, residentProfile: ResidentProfile): Promise<ElysiaResponse> {
    try {
      const response = await fetch(`${this.baseUrl}/api/elysia/request`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          resident_id: residentProfile.residentId,
          unit_number: residentProfile.unitNumber,
          request_type: request.type,
          message: request.message,
          priority: request.priority,
          preferred_contact: request.preferredContact
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Failed to submit request:', error);
      throw error;
    }
  }

  async getAmenities() {
    const response = await fetch(`${this.baseUrl}/api/elysia/amenities`);
    return await response.json();
  }

  async getCommunityInfo() {
    const response = await fetch(`${this.baseUrl}/api/elysia/community`);
    return await response.json();
  }
}

const api = new AvantResidentAPI();

// Main Elysia Chat Interface
export const ElysiaConciergeScreen: React.FC = () => {
  const [residentProfile, setResidentProfile] = useState<ResidentProfile | null>(null);
  const [currentMessage, setCurrentMessage] = useState('');
  const [selectedRequestType, setSelectedRequestType] = useState<ConciergeRequest['type']>('general_inquiry');
  const [isLoading, setIsLoading] = useState(false);
  const [chatHistory, setChatHistory] = useState<Array<{
    type: 'user' | 'elysia';
    message: string;
    timestamp: Date;
    requestId?: string;
  }>>([]);

  useEffect(() => {
    loadResidentProfile();
  }, []);

  const loadResidentProfile = async () => {
    try {
      const profile = await AsyncStorage.getItem('resident_profile');
      if (profile) {
        setResidentProfile(JSON.parse(profile));
      } else {
        // Show onboarding for new residents
        await initializeNewResident();
      }
    } catch (error) {
      console.error('Failed to load resident profile:', error);
    }
  };

  const initializeNewResident = async () => {
    // Mock profile for demo - in production, this would come from property management system
    const mockProfile: ResidentProfile = {
      unitNumber: "304",
      residentId: "AVT-RES-304-001",
      firstName: "Sarah",
      lastName: "Johnson",
      email: "sarah.johnson@email.com",
      phone: "(303) 555-0123",
      emergencyContact: "(303) 555-0456",
      moveInDate: "2025-06-01",
      leaseEndDate: "2026-05-31"
    };

    await AsyncStorage.setItem('resident_profile', JSON.stringify(mockProfile));
    setResidentProfile(mockProfile);
  };

  const sendToElysia = async () => {
    if (!currentMessage.trim() || !residentProfile || isLoading) return;

    const userMessage = {
      type: 'user' as const,
      message: currentMessage,
      timestamp: new Date()
    };

    setChatHistory(prev => [...prev, userMessage]);
    setIsLoading(true);

    const messageToSend = currentMessage;
    setCurrentMessage('');

    try {
      const request: ConciergeRequest = {
        type: selectedRequestType,
        message: messageToSend,
        priority: 'medium',
        preferredContact: 'app'
      };

      const response = await api.submitRequest(request, residentProfile);

      const elysiaMessage = {
        type: 'elysia' as const,
        message: response.response,
        timestamp: new Date(),
        requestId: response.requestId
      };

      setChatHistory(prev => [...prev, elysiaMessage]);

      // Show follow-up options if needed
      if (response.followUpNeeded) {
        Alert.alert(
          'Follow-up Scheduled',
          `I'll follow up on this request within ${response.estimatedResolutionTime}. Your request ID is ${response.requestId}.`,
          [{ text: 'OK' }]
        );
      }

    } catch (error) {
      Alert.alert('Connection Error', 'Unable to reach Elysia. Please try again.');
      console.error('Error sending message:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const RequestTypeSelector = () => (
    <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.requestTypeContainer}>
      {[
        { key: 'maintenance', label: '🔧 Maintenance' },
        { key: 'amenity_booking', label: '🏊 Amenities' },
        { key: 'package_inquiry', label: '📦 Packages' },
        { key: 'guest_access', label: '👥 Guest Access' },
        { key: 'community_info', label: '🏢 Community' },
        { key: 'general_inquiry', label: '💬 General' }
      ].map(type => (
        <TouchableOpacity
          key={type.key}
          style={[
            styles.requestTypeButton,
            selectedRequestType === type.key && styles.requestTypeButtonActive
          ]}
          onPress={() => setSelectedRequestType(type.key as ConciergeRequest['type'])}
        >
          <Text style={[
            styles.requestTypeText,
            selectedRequestType === type.key && styles.requestTypeTextActive
          ]}>
            {type.label}
          </Text>
        </TouchableOpacity>
      ))}
    </ScrollView>
  );

  if (!residentProfile) {
    return (
      <View style={styles.loadingContainer}>
        <Text style={styles.loadingText}>Loading your profile...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Elysia Concierge</Text>
        <Text style={styles.headerSubtitle}>The Avant • Unit {residentProfile.unitNumber}</Text>
      </View>

      {/* Request Type Selector */}
      <RequestTypeSelector />

      {/* Chat History */}
      <ScrollView style={styles.chatContainer} showsVerticalScrollIndicator={false}>
        {chatHistory.length === 0 && (
          <View style={styles.welcomeContainer}>
            <Text style={styles.welcomeText}>
              Hello {residentProfile.firstName}! 👋
            </Text>
            <Text style={styles.welcomeSubtext}>
              I'm Elysia, your personal concierge at The Avant. I'm here 24/7 to help with:
            </Text>
            <View style={styles.featureList}>
              <Text style={styles.featureItem}>• Maintenance requests</Text>
              <Text style={styles.featureItem}>• Amenity bookings</Text>
              <Text style={styles.featureItem}>• Package notifications</Text>
              <Text style={styles.featureItem}>• Guest access</Text>
              <Text style={styles.featureItem}>• Community information</Text>
              <Text style={styles.featureItem}>• Local recommendations</Text>
            </View>
            <Text style={styles.welcomeSubtext}>
              How can I make your day at The Avant better?
            </Text>
          </View>
        )}

        {chatHistory.map((item, index) => (
          <View key={index} style={[
            styles.messageContainer,
            item.type === 'user' ? styles.userMessage : styles.elysiaMessage
          ]}>
            <Text style={[
              styles.messageText,
              item.type === 'user' ? styles.userMessageText : styles.elysiaMessageText
            ]}>
              {item.message}
            </Text>
            <Text style={styles.messageTimestamp}>
              {item.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
            </Text>
            {item.requestId && (
              <Text style={styles.requestId}>Request ID: {item.requestId}</Text>
            )}
          </View>
        ))}

        {isLoading && (
          <View style={styles.elysiaMessage}>
            <Text style={styles.elysiaMessageText}>Elysia is thinking...</Text>
          </View>
        )}
      </ScrollView>

      {/* Input Area */}
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.textInput}
          value={currentMessage}
          onChangeText={setCurrentMessage}
          placeholder="Ask Elysia anything..."
          placeholderTextColor={AvantColors.lightText}
          multiline
          maxLength={500}
        />
        <TouchableOpacity
          style={[styles.sendButton, (!currentMessage.trim() || isLoading) && styles.sendButtonDisabled]}
          onPress={sendToElysia}
          disabled={!currentMessage.trim() || isLoading}
        >
          <Text style={styles.sendButtonText}>Send</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: AvantColors.background,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: AvantColors.background,
  },
  loadingText: {
    fontSize: 16,
    color: AvantColors.text,
  },
  header: {
    backgroundColor: AvantColors.primary,
    paddingTop: Platform.OS === 'ios' ? 50 : 30,
    paddingBottom: 15,
    paddingHorizontal: 20,
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
  },
  headerSubtitle: {
    fontSize: 14,
    color: AvantColors.secondary,
    marginTop: 2,
  },
  requestTypeContainer: {
    backgroundColor: AvantColors.lightBackground,
    paddingVertical: 10,
  },
  requestTypeButton: {
    backgroundColor: 'white',
    paddingHorizontal: 12,
    paddingVertical: 8,
    marginHorizontal: 5,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: AvantColors.secondary,
  },
  requestTypeButtonActive: {
    backgroundColor: AvantColors.accent,
    borderColor: AvantColors.accent,
  },
  requestTypeText: {
    fontSize: 12,
    color: AvantColors.text,
    fontWeight: '500',
  },
  requestTypeTextActive: {
    color: 'white',
  },
  chatContainer: {
    flex: 1,
    paddingHorizontal: 15,
  },
  welcomeContainer: {
    alignItems: 'center',
    paddingVertical: 30,
    paddingHorizontal: 20,
  },
  welcomeText: {
    fontSize: 22,
    fontWeight: 'bold',
    color: AvantColors.text,
    marginBottom: 10,
  },
  welcomeSubtext: {
    fontSize: 16,
    color: AvantColors.lightText,
    textAlign: 'center',
    lineHeight: 22,
    marginBottom: 15,
  },
  featureList: {
    alignItems: 'flex-start',
    marginBottom: 15,
  },
  featureItem: {
    fontSize: 14,
    color: AvantColors.text,
    marginBottom: 5,
  },
  messageContainer: {
    marginVertical: 5,
    paddingHorizontal: 15,
    paddingVertical: 10,
    borderRadius: 15,
    maxWidth: '85%',
  },
  userMessage: {
    backgroundColor: AvantColors.accent,
    alignSelf: 'flex-end',
  },
  elysiaMessage: {
    backgroundColor: AvantColors.lightBackground,
    alignSelf: 'flex-start',
    borderWidth: 1,
    borderColor: AvantColors.secondary,
  },
  messageText: {
    fontSize: 16,
    lineHeight: 20,
  },
  userMessageText: {
    color: 'white',
  },
  elysiaMessageText: {
    color: AvantColors.text,
  },
  messageTimestamp: {
    fontSize: 11,
    color: AvantColors.lightText,
    marginTop: 5,
  },
  requestId: {
    fontSize: 10,
    color: AvantColors.lightText,
    fontStyle: 'italic',
    marginTop: 2,
  },
  inputContainer: {
    flexDirection: 'row',
    paddingHorizontal: 15,
    paddingVertical: 10,
    backgroundColor: AvantColors.lightBackground,
    alignItems: 'flex-end',
  },
  textInput: {
    flex: 1,
    borderWidth: 1,
    borderColor: AvantColors.secondary,
    borderRadius: 20,
    paddingHorizontal: 15,
    paddingVertical: 10,
    backgroundColor: 'white',
    fontSize: 16,
    maxHeight: 100,
    marginRight: 10,
  },
  sendButton: {
    backgroundColor: AvantColors.accent,
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderRadius: 20,
  },
  sendButtonDisabled: {
    backgroundColor: AvantColors.lightText,
  },
  sendButtonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 16,
  },
});

export default ElysiaConciergeScreen;

// @progress The Avant resident mobile app - 70% complete
